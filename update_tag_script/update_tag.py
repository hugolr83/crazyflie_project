import os
import tempfile
from typing import Final, Any

import click
import yaml
from git import Repo

COMMIT_MESSAGE: Final = "chore: Updated Docker image tag"


def find_and_replace_tag(data: dict[str, Any], image_name: str, image_tag: str) -> None:
    for service, service_data in data["services"].items():
        image = service_data.get("image")
        if image_name in image:
            service_data["image"] = image_name + ":" + image_tag


def update_image_tag(file_path: str, image_name: str, image_tag: str) -> None:
    with open(file_path, "r+") as file:
        data_to_update = yaml.safe_load(file)
        find_and_replace_tag(data_to_update, image_name, image_tag)
        file.seek(0)
        file.write(yaml.dump(data_to_update))
        file.truncate()


@click.command()
@click.option("--docker-image", help="The new Docker image to update to")
@click.option("--repo-url", help="URL of the repo to update")
def update_tag(docker_image: str, repo_url: str) -> None:
    splitted_docker_image = docker_image.split(":")

    with tempfile.TemporaryDirectory() as temporary_directory:
        repo = Repo.clone_from(url=repo_url, to_path=temporary_directory)
        for root, dirs, files in os.walk(temporary_directory):
            for file in files:
                if file.startswith("docker-compose"):
                    update_image_tag(os.path.join(root, file), splitted_docker_image[0], splitted_docker_image[1])

        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name="origin")
        origin.push()


if __name__ == "__main__":
    update_tag()
