build:
	docker build -t registry.killy.space/pdfconv .

run: build
	docker run -p 8000:8000 --memory 512Mi --cpus 1.0 registry.killy.space/pdfconv

publish: build
	docker push registry.killy.space/pdfconv
