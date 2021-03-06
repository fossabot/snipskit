"""Tests for the MQTT connection settings of the `snipskit.config.SnipsConfig`
class.
"""

from snipskit.config import SnipsConfig


def test_snips_config_mqtt_default(fs):
    """Test whether a `SnipsConfig` object with default MQTT connection
    settings is initialized correctly.
    """
    config_file = '/etc/snips.toml'
    fs.create_file(config_file,
                   contents='[snips-common]\n')

    snips_config = SnipsConfig()
    assert snips_config.mqtt.broker_address == 'localhost:1883'
    assert snips_config.mqtt.auth.username is None
    assert snips_config.mqtt.auth.password is None
    assert snips_config.mqtt.auth.enabled is False
    assert snips_config.mqtt.tls.hostname is None
    assert snips_config.mqtt.tls.ca_file is None
    assert snips_config.mqtt.tls.ca_path is None
    assert snips_config.mqtt.tls.client_key is None
    assert snips_config.mqtt.tls.client_cert is None
    assert snips_config.mqtt.tls.disable_root_store is False
    assert snips_config.mqtt.tls.enabled is False


def test_snips_config_mqtt_hostname(fs):
    """Test whether a `SnipsConfig` object with specified MQTT broker address
    is initialized correctly.
    """
    config_file = '/etc/snips.toml'
    fs.create_file(config_file,
                   contents='[snips-common]\n'
                            'mqtt="mqtt.example.com:8883"\n')

    snips_config = SnipsConfig()
    assert snips_config.mqtt.broker_address == 'mqtt.example.com:8883'
    assert snips_config.mqtt.auth.username is None
    assert snips_config.mqtt.auth.password is None
    assert snips_config.mqtt.auth.enabled is False
    assert snips_config.mqtt.tls.hostname is None
    assert snips_config.mqtt.tls.ca_file is None
    assert snips_config.mqtt.tls.ca_path is None
    assert snips_config.mqtt.tls.client_key is None
    assert snips_config.mqtt.tls.client_cert is None
    assert snips_config.mqtt.tls.disable_root_store is False
    assert snips_config.mqtt.tls.enabled is False


def test_snips_config_mqtt_hostname_authentication(fs):
    """Test whether a `SnipsConfig` object with specified MQTT broker address
    and authentication is initialized correctly.
    """
    config_file = '/etc/snips.toml'
    fs.create_file(config_file,
                   contents='[snips-common]\n'
                            'mqtt="mqtt.example.com:8883"\n'
                            'mqtt_username="foobar"\n'
                            'mqtt_password="secretpassword"\n')

    snips_config = SnipsConfig()
    assert snips_config.mqtt.broker_address == 'mqtt.example.com:8883'
    assert snips_config.mqtt.auth.username == 'foobar'
    assert snips_config.mqtt.auth.password == 'secretpassword'
    assert snips_config.mqtt.auth.enabled is True
    assert snips_config.mqtt.tls.hostname is None
    assert snips_config.mqtt.tls.ca_file is None
    assert snips_config.mqtt.tls.ca_path is None
    assert snips_config.mqtt.tls.client_key is None
    assert snips_config.mqtt.tls.client_cert is None
    assert snips_config.mqtt.tls.disable_root_store is False
    assert snips_config.mqtt.tls.enabled is False


def test_snips_config_mqtt_tls(fs):
    """Test whether a `SnipsConfig` object with specified MQTT broker address
    and authentication and TLS settings is initialized correctly.
    """
    config_file = '/etc/snips.toml'
    fs.create_file(config_file,
                   contents='[snips-common]\n'
                            'mqtt="mqtt.example.com:4883"\n'
                            'mqtt_username="foobar"\n'
                            'mqtt_password="secretpassword"\n'
                            'mqtt_tls_hostname="mqtt.example.com"\n'
                            'mqtt_tls_cafile="/etc/ssl/certs/ca-certificates.crt"\n')

    snips_config = SnipsConfig()
    assert snips_config.mqtt.broker_address == 'mqtt.example.com:4883'
    assert snips_config.mqtt.auth.username == 'foobar'
    assert snips_config.mqtt.auth.password == 'secretpassword'
    assert snips_config.mqtt.auth.enabled is True
    assert snips_config.mqtt.tls.hostname == 'mqtt.example.com'
    assert snips_config.mqtt.tls.ca_file == '/etc/ssl/certs/ca-certificates.crt'
    assert snips_config.mqtt.tls.ca_path is None
    assert snips_config.mqtt.tls.client_key is None
    assert snips_config.mqtt.tls.client_cert is None
    assert snips_config.mqtt.tls.disable_root_store is False
    assert snips_config.mqtt.tls.enabled is True
