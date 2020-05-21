# aodh2sensu

Imports [OpenStack Aodh](https://docs.openstack.org/aodh/latest/) alarms into [Sensu Core](https://docs.sensu.io/sensu-core/latest/) Server.

## Use
Create an Aodh alarm from OpenStack side:
```
$ openstack alarm create \
--name cpu_hi \
--type gnocchi_resources_threshold \
--description 'CPU High Average' \
--metric cpu_util4 \
--threshold 20.0 \
--comparison-operator gt \
--aggregation-method mean \
--granularity 300 \
--evaluation-periods 1 \
--resource-type instance \
--resource-id $INSTANS_ID
```

```
$ openstack alarm list
+--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
| alarm_id                             | type                                       | name           | state             | severity | enabled |
+--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
| c466d832-cfce-4488-9726-c631800a36b1 | gnocchi_resources_threshold                | cpu_hi4        | ok                | low      | True    |
+--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
```

## Docker
To build the image:

`$ buildah build-using-dockerfile -t aodh2sensu .`

To run the image:

`$ podman run -p 50000:50000 aodh2sensu`
