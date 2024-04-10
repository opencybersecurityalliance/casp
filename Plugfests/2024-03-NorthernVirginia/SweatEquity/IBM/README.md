# IBM Sweat Equity

## stix-shifter

Leader: Md Saroer-E Azam

## kestrel

Leader: Michael Le and Xiaokui Shu

### How to display/execute the huntbook

The huntbook `complete_hunt.ipynb` can be correctly displayed and executed after [installing Kestrel runtime](https://kestrel.readthedocs.io/en/stable/installation/runtime.html) and setup [stix-shifter datasource interface](https://kestrel.readthedocs.io/en/stable/source/kestrel_datasource_stixshifter.interface.html).

To setup demo data, please go to [JHUAPL SweatEquity](https://github.com/opencybersecurityalliance/casp/tree/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/JHUAPL) and download the data in gzip, then follow the [import instruction at data-bucket-kestrel](https://github.com/opencybersecurityalliance/data-bucket-kestrel/tree/main/elasticsearch) to ingest the data into two Elasticsearch indexes (one for EDR data from sysmon, one for netflow data).

Use the following config in `stixshifter.yaml` (rename the index as you choose in ingestion):

```
profiles:

  casp2024-edr:
    connector: elastic_ecs
    connection:
      host: rainbow.sl.cloud9.ibm.com
      port: 9200
      selfSignedCert: false
      indices: casp2024-20240306-sysmon-2
      options:
        retrieval_batch_size: 10000
    config:
      auth:
        id: xxx
        api_key: xxx

  casp2024-netflow:
    connector: elastic_ecs
    connection:
      host: rainbow.sl.cloud9.ibm.com
      port: 9200
      selfSignedCert: false
      indices: casp2024-20240306-netflow-2
      options:
        retrieval_batch_size: 10000
    config:
      auth:
        id: xxx
        api_key: xxx

```

Now you are ready to run `complete_hunt.ipynb` as well as the huntflows executed by OC2.

### Unit Huntflows

These huntflows can be executed using Kestrel command-line utility, or by an OC2 consumer.
- `oc2-hunt-1.hf`
- `oc2-hunt-2.hf`
- `oc2-hunt-3.hf`
- `oc2-hunt-4.hf`

Check `run_test.sh` for more details.
