# Hosting APIs in Azure

If you want to host a [FastAPI][301] app in Azure you'll face a [bewildering array of options][302] seemingly organized by throwing stuff against the wall and seeing what sticks.

- Azure App Service using the Web App for Containers feature
- Function Apps
- Container Apps
- Container Instances
- Azure Kubernetes Service


## Container Apps

Want to just push a container somewhere and have someone else manage the environment? That's the idea behind Azure Container Apps.



[301]: https://fastapi.tiangolo.com/
[302]: https://learn.microsoft.com/en-us/azure/developer/python/containers-in-azure-overview-python?tabs=vscode-ide#deployment-container-options-in-azure
[303]: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
[304]: https://learn.microsoft.com/en-us/azure/container-apps/client-certificate-authorization
