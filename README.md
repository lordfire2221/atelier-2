# Etape 1
pour mon ce tp j'ai choisi d'utiliser comme outils github-cli et avec comme repo YetiforceCompany/YetiForce
j'ai téléchager le github-cli de windows sur github, puis je me suis authentifié avec la commande gh auth login 
par la suite j'ai eu quelque problème pour récupérer les informations sur le repo yetiforce donc, j'ai du refaire un token possédant ces droits puis, je me suis re-authentifié avec ma clé token.
Par le suite j'ai utilisé la commande suite pour recupérer les informations sur le repo yetiforce en fichier json : 
```
gh repo view  YetiforceCompany/YetiForce  --json  archivedAt,assignableUsers,codeOfConduct,contactLinks,createdAt,defaultBranchRef,deleteBranchOnMerge,description,diskUsage,hasDiscussionsEnabled,hasIssuesEnabled,hasProjectsEnabled,hasWikiEnabled,homepageUrl,id,isArchived,isBlankIssuesEnabled,isEmpty,isFork,isInOrganization,isMirror,isPrivate,isSecurityPolicyEnabled,isTemplate,isUserConfigurationRepository,issueTemplates,issues,labels,languages,latestRelease,licenseInfo,mentionableUsers,mergeCommitAllowed,milestones,mirrorUrl,name,nameWithOwner,openGraphImageUrl,owner,parent,primaryLanguage,projects,projectsV2,pullRequestTemplates,pullRequests,pushedAt,rebaseMergeAllowed,repositoryTopics,securityPolicyUrl,squashMergeAllowed,sshUrl,stargazerCount,templateRepository,updatedAt,url,usesCustomOpenGraphImage,viewerCanAdminister,viewerDefaultCommitEmail,viewerDefaultMergeMethod,viewerHasStarred,viewerPermission,viewerPossibleCommitEmails,viewerSubscription,visibility,watchers >  repo_data.json

```
