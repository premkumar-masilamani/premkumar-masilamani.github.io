# Phony targets ensure commands associated with target are run regardless of file state.
.PHONY: run
run:
	@echo "Deleting the _site folder..."
	rm -rf _site
	echo "Starting new container: premkumar-masilamani-blog"; \
	docker run --name premkumar-masilamani-blog \
		-e JEKYLL_ENV=docker \
		-e PAGES_REPO_NWO=premkumar-masilamani/premkumar-masilamani.github.io \
		-p 4000:4000 \
		-v $${PWD}:/srv/jekyll \
		jekyll/jekyll:4.2.0 \
		jekyll serve --config _local-config.yml --watch --incremental --drafts;
