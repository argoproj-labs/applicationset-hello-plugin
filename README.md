# ApplicationSet Hello Plugin

This is an example ApplicationSet plugin generator.

## Testing

First, install Argo CD on your cluster.

Second, install the plugin's manifests. The manifests assume that Argo CD is installed in the `argocd` namespace and 
that you want to install the plugin Deployment in the `applicationset-hello-plugin` namespace.

```bash
kubectly apply -k manifests
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: myplugin
spec:
  generators:
    - plugin:
        name: my-plugin
        configMapRef: applicationset-hello-plugin
  template:
    metadata:
      name: 'from-appset-{{hello}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/argoproj/argocd-example-apps.git
        path: .
      destination:
        server: https://kubernetes.default.svc
        namespace: default
```
