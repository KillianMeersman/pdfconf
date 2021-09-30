build:
	docker build -t registry.killy.space/pdfconv .

run: build
	docker run -p 8000:8000 registry.killy.space/pdfconv

publish: build
	docker push registry.killy.space/pdfconv
