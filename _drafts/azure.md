---
layout: post
title:  "Azure with Python"
date:   2021-04-01 14:55:00 +1300
categories: devops
---

Microsoft technology is very entrenched in the Wellington tech scene. Below are notes taken along the journey up the learning curve of Azure from a data and Python perspective. Now that the [BDFL Emeritus has joined up][100], one would hope that Python will get first class treatment on Azure.


## The Good Parts

- Virtual Machines (VMs)
- Blob containers (Buckets)
- Service Bus (Message Queue)
- Functions
- Batch ?
- Container Instances ?
- Container Registry ?
- Key Vault ?
- PostgreSQL


## The non-good parts

Microsoft's cloud offering could hardly help being influenced by its history of proprietary point-n-click software. No doubt, cloud migration from legacy products represents a huge part of Azure's success.

Also, technology moves fast and Microsoft is not a young company. Come to think of it, I'm not young anymore either, but anyway... Parts of Azure show signs of being alpha-quality software rushed into production.

I'm hoping I'll learn to recognize and avoid technologies in either of these categories. But, so far, I've had to struggle a bit before it becomes clear whether I'm climbing a steep learning curve for a solid technology or falling into a pothole of half-baked jank.


## Auth

Bad examples abound. Read [How to authenticate and authorize Python apps on Azure][106] on how to use [DefaultAzureCredential][108] and managed identities.

Lots of the examples use either connection strings or [shared access signatures][101], which I think steers you in the wrong direction. You can get either SAS tokens and SAS URIs from the Azure portal. Most of the SDK objects have a constructor that takes an SAS URI, for example [ContainerClient.from_container_url(sas_url)][102]. The point of SAS tokens eludes me.

Code running inside Azure should probably use managed identities, as in this [example][107].


## Running Python code

How would you deploy a Python code in Azure? Specifically, I like to write APIs in [FastAPI][301]. Confusingly, there are at least 5 different [options for deploying containers in Azure][302]. I wish there was guidance of this form: If you want to do X, the best choice is Y.



## Karma

Ever since they became an underdog, I keep rooting for a Microsoft comeback. I'm glad to see Azure doing well and R and Python finding a place in Redmond. I'm hopeful that Microsoft will be a good steward of GitHub. Spending some time as an underdog is good for the soul. Microsoft's reemergence could provide some much-needed balance relative to the other tech giants.


[100]: https://twitter.com/gvanrossum/status/1326932991566700549
[101]: https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview
[102]: https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient?view=azure-python#azure_storage_blob_ContainerClient_from_container_url
[105]: https://docs.microsoft.com/en-us/azure/container-instances/container-instances-overview
[106]: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate
[107]: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate?view=azure-python#authenticate-with-defaultazurecredential
[108]: https://docs.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python
[109]: https://github.com/Azure/azure-sdk-for-python/issues/18337



https://www.tutlinks.com/deploy-fastapi-on-azure/



https://www.thoughtworks.com/radar/platforms/azure-machine-learning



https://markheath.net/post/user-delegation-sas


[201]: https://www.alexhudson.com/2021/09/17/its-tough-being-an-azure-fan/



https://marileeturscak.com/posts/app-registrations-enterprise-applications-service-principals/

[301]: https://fastapi.tiangolo.com/
[302]: https://learn.microsoft.com/en-us/azure/developer/python/containers-in-azure-overview-python?tabs=vscode-ide#deployment-container-options-in-azure
[303]: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
