.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS
run: ## build and run the containers
	cd docker; docker-compose up -d;

stop: ## stop running containers
	cd docker; docker-compose down;

flask-app: ## enter the bash of judger-app container
	docker exec -it flask_app sh

cp: ## commit all and push to github master
	git add .; git commit; git push

rebuild: move-images ## rebuild new images and run
	make run

move-images: stop ## remove images
	docker image rm flask_demo
