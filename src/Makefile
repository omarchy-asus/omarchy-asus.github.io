# Rebuild index.html from the template, the chart data and the wordmark.
../index.html: template.html charts.py wordmark.py build.py
	python3 charts.py charts.json
	python3 wordmark.py > wordmark.svg
	python3 build.py . ../index.html
	rm -f charts.json wordmark.svg
