PYTHON ?= python3

.PHONY: python-checks exact symbolic downstream tests generate verify-generated manuscript-audit lean manuscript all clean

python-checks: exact symbolic downstream tests

exact:
	$(PYTHON) code/uniform_game_cleanroom.py

symbolic:
	$(PYTHON) code/symbolic_reconstruction.py

downstream:
	$(PYTHON) code/downstream_impact_symbolic.py

tests:
	PYTHONPATH=code $(PYTHON) -m unittest discover -s tests -v

generate:
	$(PYTHON) code/generate_stage09_artifacts.py --output generated

verify-generated:
	$(PYTHON) code/verify_generated_artifacts.py

manuscript-audit:
	$(PYTHON) code/audit_manuscript_claims.py

lean:
	cd formal && lake update && lake exe cache get && lake build

manuscript: manuscript-audit
	mkdir -p build/manuscript
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build/manuscript manuscript/main.tex
	bibtex build/manuscript/main
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build/manuscript manuscript/main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build/manuscript manuscript/main.tex

all: python-checks generate verify-generated lean manuscript

clean:
	rm -rf build .stage09-regenerate
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
