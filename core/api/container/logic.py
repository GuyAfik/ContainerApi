"""
Here resides the business logic layer.
"""
import subprocess

from core.api.common.middleware.response import response_decorator
from core.api.common.validation import BaseContainerSchema, validate_request_body
from core import docker_client


@response_decorator(code=200)
@validate_request_body(schema_class=BaseContainerSchema)
def run_container(**container_data):
    """
    Creates & runs a new container.

    Keyword Arguments:
        name (str): container name.
        image (str): container image.
        ports (dict): container ports.
        command (str): container command.
        detach (bool): detached state of the container, True to detach, False otherwise.

    Json examples:
        {
            "name": "my_nginx",
            "image": "nginx",
            "ports": {
                "22222/tcp": 22222
            }
        }

        {
            "name": "hello-world-container",
            "image": "hello-world",
            "detach": false
        }

    Curl examples:

        You can run container with any image that you like, here are two examples:

        Hello world container:

        curl -d '{"name": "my_nginx", "image": "hello-world"}' -H "Content-Type: application/json" -X POST
        http://<server_ip>:<server_port>/container

        nginx container:

        curl -d '{"name": "my_nginx", "image": "nginx", "ports": {"22222/tcp": 22222}, "detach": true}' -H
        "Content-Type: application/json" -X POST http://<server_ip>:<server_port>/container

    Notes:
        name & image json fields when trying to run a container are required! even though name can be automatically
        created by the docker.
        In my opinion its important to have a container meaningful name in order to know what it does.

    Returns:
        dict: container information.
    """
    container = docker_client.containers.run(**container_data)

    if not container_data.get("detach"):  # this means that we got back the container logs instead of the object.
        container = docker_client.containers.get(container_id=container_data.get("name"))

    return container.attrs


@response_decorator(code=200)
def get_latest_running_container(limit=1):
    """
    Gets the latest running container.

    Args:
        limit (int): the amount of last containers to get.

    Curl Example:

        curl http://<server_ip>:<server_port>/container would produce the last container information:

        {
          "AppArmorProfile": "",
          "Args": [],
          "Config": {
            "AttachStderr": false,
            "AttachStdin": false,
            "AttachStdout": false,
            "Cmd": [
              "/hello"
            ],
            "Domainname": "",
            "Entrypoint": null,
            "Env": [
              "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "ExposedPorts": {
              "33333/tcp": {}
            },
            "Hostname": "0d6f47ee4142",
            "Image": "hello-world",
            "Labels": {},
            "OnBuild": null,
            "OpenStdin": false,
            "StdinOnce": false,
            "Tty": false,
            "User": "",
            "Volumes": null,
            "WorkingDir": ""
          },
          "Created": "2021-07-10T18:56:01.61392824Z",
          "Driver": "overlay2",
          "ExecIDs": null,
          "GraphDriver": {
            "Data": {
              "LowerDir": "/var/lib/docker/overlay2/166a60a5f97c401041ec8e6cc05181f2de82807af52ee01249e365e3ac855b69-
              init/diff:/var/lib/docker/overlay2/1615fd8772d89f1d772044e33a9431b7542b659c7672fb9f91861ef8b3bbdceb/diff",
              "MergedDir": "/var/lib/docker/overlay2/
              166a60a5f97c401041ec8e6cc05181f2de82807af52ee01249e365e3ac855b69/merged",
              "UpperDir": "/var/lib/docker/overlay2/
              166a60a5f97c401041ec8e6cc05181f2de82807af52ee01249e365e3ac855b69/diff",
              "WorkDir": "/var/lib/docker/overlay2/
              166a60a5f97c401041ec8e6cc05181f2de82807af52ee01249e365e3ac855b69/work"
            },
            "Name": "overlay2"
          },
          "HostConfig": {
            "AutoRemove": false,
            "Binds": null,
            "BlkioDeviceReadBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceWriteIOps": null,
            "BlkioWeight": 0,
            "BlkioWeightDevice": null,
            "CapAdd": null,
            "CapDrop": null,
            "Cgroup": "",
            "CgroupParent": "",
            "CgroupnsMode": "private",
            "ConsoleSize": [
              0,
              0
            ],
            "ContainerIDFile": "",
            "CpuCount": 0,
            "CpuPercent": 0,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpuShares": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "Devices": null,
            "Dns": null,
            "DnsOptions": null,
            "DnsSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IOMaximumBandwidth": 0,
            "IOMaximumIOps": 0,
            "IpcMode": "private",
            "Isolation": "",
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "Links": null,
            "LogConfig": {
              "Config": {},
              "Type": "json-file"
            },
            "MaskedPaths": [
              "/proc/asound",
              "/proc/acpi",
              "/proc/kcore",
              "/proc/keys",
              "/proc/latency_stats",
              "/proc/timer_list",
              "/proc/timer_stats",
              "/proc/sched_debug",
              "/proc/scsi",
              "/sys/firmware"
            ],
            "Memory": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "NanoCpus": 0,
            "NetworkMode": "default",
            "OomKillDisable": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "PidsLimit": null,
            "PortBindings": {
              "33333/tcp": [
                {
                  "HostIp": "",
                  "HostPort": "22222"
                }
              ]
            },
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyPaths": [
              "/proc/bus",
              "/proc/fs",
              "/proc/irq",
              "/proc/sys",
              "/proc/sysrq-trigger"
            ],
            "ReadonlyRootfs": false,
            "RestartPolicy": {
              "MaximumRetryCount": 0,
              "Name": ""
            },
            "Runtime": "runc",
            "SecurityOpt": null,
            "ShmSize": 67108864,
            "UTSMode": "",
            "Ulimits": null,
            "UsernsMode": "",
            "VolumeDriver": "",
            "VolumesFrom": null
          },
          "HostnamePath": "/var/lib/docker/containers/
          0d6f47ee41427ddbd249314d1dbc61df15d73018ff100a43f3c6a9767f9ce317/hostname",
          "HostsPath": "/var/lib/docker/containers/
          0d6f47ee41427ddbd249314d1dbc61df15d73018ff100a43f3c6a9767f9ce317/hosts",
          "Id": "0d6f47ee41427ddbd249314d1dbc61df15d73018ff100a43f3c6a9767f9ce317",
          "Image": "sha256:d1165f2212346b2bab48cb01c1e39ee8ad1be46b87873d9ca7a4e434980a7726",
          "LogPath": "/var/lib/docker/containers/0d6f47ee41427ddbd249314d1dbc61df15d73018ff100a43f3c6a9767f9ce317/
          0d6f47ee41427ddbd249314d1dbc61df15d73018ff100a43f3c6a9767f9ce317-json.log",
          "MountLabel": "",
          "Mounts": [],
          "Name": "/bla23",
          "NetworkSettings": {
            "Bridge": "",
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "HairpinMode": false,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "MacAddress": "",
            "Networks": {
              "bridge": {
                "Aliases": null,
                "DriverOpts": null,
                "EndpointID": "",
                "Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "IPAMConfig": null,
                "IPAddress": "",
                "IPPrefixLen": 0,
                "IPv6Gateway": "",
                "Links": null,
                "MacAddress": "",
                "NetworkID": "72c7973629f0959cb75da8e765cb5045ff68e0ada4cbf925714451990bf5495f"
              }
            },
            "Ports": {},
            "SandboxID": "5e4ce7a9c3ef7e0e7bc3fbd8a4cfba8ae1a54db250a95afec909c60529b00527",
            "SandboxKey": "/var/run/docker/netns/5e4ce7a9c3ef",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null
          },
          "Path": "/hello",
          "Platform": "linux",
          "ProcessLabel": "",
          "ResolvConfPath": "/var/lib/docker/containers/
          0d6f47ee41427ddbd249314d1dbc61df15d73018ff100a43f3c6a9767f9ce317/resolv.conf",
          "RestartCount": 0,
          "State": {
            "Dead": false,
            "Error": "",
            "ExitCode": 0,
            "FinishedAt": "2021-07-10T18:56:01.995694809Z",
            "OOMKilled": false,
            "Paused": false,
            "Pid": 0,
            "Restarting": false,
            "Running": false,
            "StartedAt": "2021-07-10T18:56:01.995816519Z",
            "Status": "exited"
          }
        }

    Returns:
        dict: last container information in case found, empty dict otherwise.
    """
    container = docker_client.containers.list(limit=limit)
    if container:
        return container[0].attrs
    return {}


@response_decorator(code=200)
def get_all_containers():
    """
    Gets all the containers.

    Returns:
         list[dict]: all containers.
    """
    return [container.attrs for container in docker_client.containers.list(all=True)]


def sample_services_config(file_name='docker-compose.yml'):
    """
    Samples services configurations, This function will be executed as long as the server is active.
    Updates the services configurations according to the file configuration using docker-compose.

    Important note:
        there is no correlation between what the POST api produces to what the configuration file holds.
        so if we try to create container through the api, we will not see this in docker-compose config file or the
        other way around.

        GET on the other hand will show the last created container/or all containers that were created even with
        docker compose.

        The print statements are simply just to understand what's going on with the application, for example it will
        alarm in case of a misconfiguration of the docker-compose yaml file.

    Args:
        file_name (str): docker compose file name.
    """
    docker_compose_cmd = ['docker-compose', 'up', '-d', '--remove-orphans']

    try:
        with open(file=file_name) as file:
            file_content = file.read()
            process = subprocess.run(
                docker_compose_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            if not process.returncode:  # code = 0 ---> means operation is successful, otherwise operation failed.
                print(f"docker-compose was updated successfully using this file:\n{file_content}")
            else:
                print(
                    f"error occurred while trying to update containers configurations, "
                    f"error:\n{process.stderr.decode('utf-8')}"
                )
                print(f"Please make sure your file is configured correctly\n{file_content}")
    except FileNotFoundError:
        print(f"file named {file_name} was not found!")
