# Phony targets ensure commands associated with target are run regardless of file state.
.PHONY: run
run:
	@echo "Deleting _site folder..."
	rm -rf _site
	@CONTAINER_ID=$$(docker ps -aq -f name=premkumar-masilamani); \
	if [ ! -z "$$CONTAINER_ID" ]; then \
		echo "Stopping and removing existing container: premkumar-masilamani (ID: $$CONTAINER_ID)"; \
		docker stop premkumar-masilamani >/dev/null 2>&1 || true; \
		docker rm premkumar-masilamani; \
	fi; \
	echo "Starting new container: premkumar-masilamani"; \
	docker run -d --name premkumar-masilamani \
		-e JEKYLL_ENV=docker \
		-e PAGES_REPO_NWO=premkumar-masilamani/premkumar-masilamani.github.io \
		-p 4000:4000 \
		-v $${PWD}:/srv/jekyll \
		jekyll/jekyll:4.2.0 \
		jekyll serve --config _local-config.yml --watch --incremental --drafts; \
	NEW_CONTAINER_ID=$$(docker ps -q -f name=premkumar-masilamani); \
	echo "Container started: premkumar-masilamani (ID: $$NEW_CONTAINER_ID)"
