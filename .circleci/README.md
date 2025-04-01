# CircleCI Configuration

This repository contains a CircleCI configuration file (`config.yml`) that defines the workflow and jobs for building and publishing addons images.

## Workflow

The workflow is named `build-and-publish-addons-images` and consists of two jobs:

1. `install-yq`: This job installs the `yq` orb using the `arm-executor` executor.

2. `docker/publish`: This job publishes the addons images based on the specified matrix parameters.

## Jobs

### `install-yq`

This job is responsible for installing the `yq` orb using the `arm-executor` executor.

### `docker/publish`

This job publishes the addons images based on the specified matrix parameters. It performs the following steps:

1. Checkout the codebase.
2. Set environment variables `BASE_IMAGE` and `TAG` based on the contents of the `build.yml` and `config.yml` files respectively.
3. Build and publish the addon image using the specified `docker-context`, `extra_build_args`, `image`, and `tag`.

## Matrix Parameters

The `matrix` section within the `docker/publish` job defines a matrix of parameters for the job. It includes the following parameters:

- `path`: Specifies the path of the addon.
- `context`: Specifies the context of the addon.
- `executor`: Specifies the executor to be used for building the addon.

## Exclusions

The `exclude` section within the `matrix` specifies a list of combinations to exclude from the job. These combinations are excluded based on the `path`, `context`, and `executor` parameters.

## Orbs

The repository imports two orbs:

- `docker`: The `circleci/docker` orb provides Docker-related functionality.
- `yq`: The `nikkei/rnikkei-yq` orb provides YAML processing functionality.

Please note that this README is generated based on the provided YAML configuration and may not include all the details or specifics of your actual implementation. Feel free to modify it as per your requirements.