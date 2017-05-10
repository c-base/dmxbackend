# -*- coding; utf-8 -*-
import pytest
from unittest.mock import MagicMock, Mock
from dmxbackend.mqtt import AsyncMQTT


@pytest.fixture
def mock_mqtt():
    mqtt = AsyncMQTT(client=Mock())
    return mqtt
    
    
def test_on_connect(mock_mqtt):
    #result = mock_mqtt.on_connect() #   client, userdata, flags, rc):
    pass


def test_on_message(mock_mqtt):
    client = None
    userdata = None
    message = Mock()
    message.payload = MagicMock()
    result = mock_mqtt.on_message(client, userdata, message) #):
    #self.message_queue.append(message.payload.decode('utf8'))


