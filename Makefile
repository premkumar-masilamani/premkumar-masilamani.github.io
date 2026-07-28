.PHONY: run run-apple run-docker

run: run-apple

run-apple:
	@echo "Deleting the _site folder..."
	rm -rf _site
	@if ! container system status 2>/dev/null | grep -q "running"; then \
		echo "Starting container system service..."; \
		container system start; \
	fi
	@if container ls -a | grep -q premkumar-masilamani-blog; then \
		echo "Stopping existing container..."; \
		container rm -f premkumar-masilamani-blog >/dev/null 2>&1 || true; \
	fi
	echo "Starting new container: premkumar-masilamani-blog"; \
	container run --platform linux/amd64 --name premkumar-masilamani-blog \
		-e JEKYLL_ENV=docker \
		-e PAGES_REPO_NWO=premkumar-masilamani/premkumar-masilamani.github.io \
		-p 4000:4000 \
		-v $${PWD}:/srv/jekyll \
		jekyll/jekyll:4.2.0 \
		jekyll serve --config _local-config.yml --watch --incremental --drafts 2>/dev/null & \
		container_pid=$$!; \
		trap "echo 'Stopping container...'; container rm -f premkumar-masilamani-blog >/dev/null 2>&1 || true; exit 0" INT TERM; \
		wait $$container_pid

run-docker:
	@echo "Deleting the _site folder..."
	rm -rf _site
	@if docker ps -aq --filter "name=premkumar-masilamani-blog" | grep -q .; then \
		echo "Stopping existing container..."; \
		docker stop premkumar-masilamani-blog && docker rm premkumar-masilamani-blog; \
	fi
	echo "Starting new container: premkumar-masilamani-blog"; \
	docker run --name premkumar-masilamani-blog \
		-e JEKYLL_ENV=docker \
		-e PAGES_REPO_NWO=premkumar-masilamani/premkumar-masilamani.github.io \
		-p 4000:4000 \
		-v $${PWD}:/srv/jekyll \
		jekyll/jekyll:4.2.0 \
		jekyll serve --config _local-config.yml --watch --incremental --drafts & \
		container_pid=$$!; \
		trap "echo 'Stopping container...'; docker stop premkumar-masilamani-blog && docker rm premkumar-masilamani-blog; exit 0" INT TERM; \
		wait $$container_pid

