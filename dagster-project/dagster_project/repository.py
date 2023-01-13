from dagster import load_assets_from_package_module, repository

from dagster_project import assets


@repository
def dagster_project():
    return [load_assets_from_package_module(assets)]
