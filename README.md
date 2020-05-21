# aodh2sensu

Imports [OpenStack Aodh](https://docs.openstack.org/aodh/latest/) alarms into [Sensu Core](https://docs.sensu.io/sensu-core/latest/) Server.

## Install

`pip3 install -r /tmp/requirements.txt`

## Use

- Run the `aodh2sensu` proxy. It must be run in a server reachable from OpenStack controllers and with access to the Sensu Server.

   `$ python3 aodh2sensu`

- Create an Aodh alarm from OpenStack side. This alarm will trigger an HTTP POST message to the `aodh2sensu` proxy:
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
   --resource-id $INSTANS_ID \
   --alarm-action 'http://x.y.z.w:50000' \
   --ok-action 'http://x.y.z.w:50000' \
   --insufficient-data-action 'http://x.y.z.w:50000'
   ```
where `x.y.z.w` is the IP address of the server running `aodh2sensu` proxy.

- Confirm the alarm transitions from `insufficient_data` state to `ok` state:
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
