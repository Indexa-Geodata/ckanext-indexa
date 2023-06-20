# -*- coding: utf-8 -*-

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.helpers import literal


def get_csv_id(resources):
    for resource in resources:
        try:
            if "CSV" in resource["format"]:
                return resource["id"]
        except:
            if 'CSV' in resource.format:
                return resource.id


def get_dataset_url(url, name):
    index = url.find("<a ") + 3
    result = url[:index] + "class=label" + url[index:]
    # result = result.replace(name, 'Informacion')
    index_2 = result.find(">")
    result = result[:index_2] + result[index_2:].replace(name, "Información")
    return literal(result)


def get_url_tag_org(url, tag):
    index = url.find("organization/")
    organization = url[index + 13 :]
    end_index = len(organization)
    if "/" in organization:
        end_index = organization.find("/")
    if "?" in organization:
        end_index = organization.find("?")
    organization = organization[:end_index]
    return "/dataset?tags={0}&organization={1}".format(tag, organization)


def build_custom_nav_icon(string):
    return literal(
        '{0}class="a-color"{1}'.format(
            string[: string.find("a href") + 2], string[string.find("a href") + 2 :]
        )
    )


def custom_read_more(string):
    return string


def custom_tags():
    return {
        "cienciaytecnologia": "Ciencia y Tecnología",
        "comercio": "Comercio",
        "culturayocio": "Cultura y Ocio",
        "demografia": "Demografía",
        "deportes": "Deportes",
        "economia": "Economía",
        "medioambiente": "Medio ambiente",
        "mediorural": "Medio rural",
        "salud": "Salud",
        "sectorpublico": "Sector público",
        "seguridad": "Seguridad",
        "sociedadybienestar": "Sociedad y Bienestar",
        "educacion": "Educación",
        "empleo": "Empleo",
        "energia": "Energía",
        "hacienda": "Hacienda",
        "industria": "Industria",
        "legislacionyjusticia": "Legislación y Justicia",
        "transporte": "Transporte",
        "turismo": "Turismo",
        "urbanismoeinfraestructura": "Urbanismo e Infraestructura",
        "vivienda": "Vivienda",
    }


class IndexaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("fanstatic", "indexa")

    def get_helpers(self):
        return {
            "custom_tags": custom_tags,
            "build_custom_nav_icon": build_custom_nav_icon,
            "get_url_tag_org": get_url_tag_org,
            "get_dataset_url": get_dataset_url,
            "get_csv_id": get_csv_id,
        }
