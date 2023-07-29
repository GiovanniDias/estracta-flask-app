def test_environment(app):
    assert app.config['ENV_STATUS'] == "On testing"
    assert app.config.current_env == "testing"


def test_dynaconf_settings_is_app_settings_object(app):
    from dynaconf import settings

    assert settings is app.config._settings
    assert settings.ENV_STATUS == app.config["ENV_STATUS"]
    assert settings.current_env == app.config.current_env
