import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def custom_tags():
    return {'cienciaytecnologia': 'Ciencia y Tecnología', 'comercio': 'Comercio', 'culturayocio': 'Cultura y Ocio',
            'demografia': 'Demografía', 'deportes': 'Deportes', 'economia': 'Economía',
            'medioambiente': 'Medio ambiente', 'mediorural': 'Medio rural', 'salud': 'Salud',
            'sectorpublico': 'Sector público', 'seguridad': 'Seguridad', 'sociedadybienestar': 'Sociedad y Bienestar',
            'educacion': 'Educación', 'empleo': 'Empleo', 'energia': 'Energía', 'hacienda': 'Hacienda',
            'industria': 'Industria', 'legislacionyjusticia': 'Legislación y Justicia', 'transporte': 'Transporte',
            'turismo': 'Turismo', 'urbanismoeinfraestructura': 'Urbanismo e Infraestructura', 'vivienda': 'Vivienda'}

class IndexaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
                             'indexa')

    def get_helpers(self):
        return {'custom_tags': custom_tags}
