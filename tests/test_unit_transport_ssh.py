from itoolkit import iToolKit
from itoolkit.transport import SshTransport


def mock_ssh(mocker):
    client = mocker.MagicMock()

    channels = (
        mocker.MagicMock(),
        mocker.MagicMock(closed=True),
        mocker.MagicMock(closed=True),
    )

    client.channels = channels

    client.exec_command.return_value = channels

    return client


def test_ssh_transport_minimal(mocker):
    ssh_client = mock_ssh(mocker)

    transport = SshTransport(ssh_client)
    tk = iToolKit()
    transport.call(tk)

    command = "/QOpenSys/pkgs/bin/xmlservice-cli"
    ssh_client.exec_command.assert_called_once_with(command)
