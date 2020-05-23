# aodh2sensu

Imports [OpenStack Aodh](https://docs.openstack.org/aodh/latest/) alarms into [Sensu Core](https://docs.sensu.io/sensu-core/latest/) Server.

## Install

`$ pip3 install -r ./requirements.txt`

## Use

```
Usage: aodh2sensu [options]

Imports OpenStack Aodh alarms into Sensu Core Server.

Options:
  -h, --help            show this help message and exit
  --sensu-url URL       if not specified, defaults to localhost:4567
```

- Run the `aodh2sensu` proxy. `sensu_url` must point to the sensu server. The proxy must be run in a server reachable from OpenStack controllers and with access to the Sensu Server (for example, the Sensu Server itself).

   `$ ./aodh2sensu`

- Create an Aodh alarm from OpenStack side. This example alarm will trigger an HTTP POST message to the `aodh2sensu` proxy whenever the cpu utilization of $INSTANCE_ID goes above 20%:
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
   --resource-id $INSTANSCE_ID \
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
   
- Generate load in the instance above the 20% threeshold, and wait for the alarm to transitition to `alarm` state:
   ```
   $ openstack alarm list
   +--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
   | alarm_id                             | type                                       | name           | state             | severity | enabled |
   +--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
   | c466d832-cfce-4488-9726-c631800a36b1 | gnocchi_resources_threshold                | cpu_hi4        | alarm             | low      | True    |
   +--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+

   ```

- Check the alarm from the Uchiwa dashboard:
![Screenshot 1 of the Uchiwa dashboard](https://github.com/josecastillolema/aodh2sensu/blob/master/doc/img/screenshot1.png)
![Screenshot 2 of the Uchiwa dashboard](https://github.com/josecastillolema/aodh2sensu/blob/master/doc/img/screenshot2.png)


- Stop the load generation in the instance, wait for the alarm to transition back to `ok` state:
   ```
   $ openstack alarm list
   +--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
   | alarm_id                             | type                                       | name           | state             | severity | enabled |
   +--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
   | c466d832-cfce-4488-9726-c631800a36b1 | gnocchi_resources_threshold                | cpu_hi4        | ok                | low      | True    |
   +--------------------------------------+--------------------------------------------+----------------+-------------------+----------+---------+
   ```

- Check the new state of the sensu alert:
![Screenshot 3 of the Uchiwa dashboard](https://github.com/josecastillolema/aodh2sensu/blob/master/doc/img/screenshot3.png)

- Confirm it has dissapeared from the list of active alerts:
![Screenshot 4 of the Uchiwa dashboard](https://github.com/josecastillolema/aodh2sensu/blob/master/doc/img/screenshot4.png)


## Docker
To build the image:

`$ buildah build-using-dockerfile -t aodh2sensu .`

To run the image:

```
$ podman run -p 50000:50000 aodh2sensu                                 or
$ podman run -p 50000:50000 -e SENSU_URL=x.y.z.w:p aodh2sensu
```

Check logs:
`$ podman logs `
