APP_NAME=log_mailer
ENV_FILE=./config.env

build: ## Build container
	docker build -t $(APP_NAME) .

run: ## Run container 
	-docker run --rm -d --env-file=$(ENV_FILE) -v /:/host --name="$(APP_NAME)" $(APP_NAME) 

stop:
	-docker stop $(APP_NAME)

up: build run

