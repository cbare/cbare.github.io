# Auth with Azure Active Directory for command-line Python script

What is the best solution for authentication and authorization? I don't know, but we're using Microsoft's [Azure Active Directory][1].


## Trust, don't verify

One aspect of AAD that's generated a lot of [confusion and controversy][2] is the JWTs for the Graph API. They look like standard JWTs, but there's a little extra bit of Redmond magic ([a nonce][4]) that causes signature verification to fail. Their view seems to be that the access token belongs to Azure AD and its internals are an implementation detail subject to change. Because we are not the intended audience of that token, we shouldn't look inside or attempt to verify. We should instead treat the token as opaque and get user information through the AAD Graph API.

Apparently, you can perform [Azure Active Directory OAuth2 JWT Token Validation with Python][3], provided you've set the scope properly to indicate your app as the intended audience. I have yet to figure out what "properly" means in this context.

You can get public keys to verify signatures at a URL of the form identified by a "wid" in the JWT's header.

```py
f"https://login.microsoftonline.com/{tenant_id}/discovery/keys?appid={app_id}"
```


[1]: https://docs.microsoft.com/en-us/azure/active-directory/develop/
[2]: https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet/issues/609
[3]: https://aboutsimon.com/blog/2017/12/05/Azure-ActiveDirectory-JWT-Token-Validation-With-Python.html
[4]: https://github.com/AzureAD/microsoft-authentication-library-for-js/issues/815
[5]: https://docs.python.org/3/library/http.server.html
[6]: https://pyjwt.readthedocs.io/en/stable/index.html
[7]: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-group-claims

