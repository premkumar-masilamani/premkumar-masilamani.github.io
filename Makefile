.PHONY: run
run:
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
