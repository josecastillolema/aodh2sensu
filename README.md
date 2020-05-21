# aodh2sensu

Imports [OpenStack Aodh](https://docs.openstack.org/aodh/latest/) alarms into [Sensu Core](https://docs.sensu.io/sensu-core/latest/) Server.

## Docker
To build the image:

`$ buildah build-using-dockerfile -t aodh2sensu .`

To run the image:

`$ podman run -p 50000:50000 aodh2sensu`
