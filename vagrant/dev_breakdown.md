# Development Breakdown

Over the course of development, The Movie Site went through many feature changes along the way. The more interesting parts include video modals which I had no prior experience with and the Redis cache which required JSON encoding/decoding.

This all took place over the course of a few weeks before authoring this breakdown; however, the site continues to gain features and undergo stylistic changes. The latest was the initially-planned ability to fetch YouTube URL's for new movies rather than input them manually.

The primary issue with that was a lack of practice, but it was ultimately pretty straight forward. I simply had to find the various means in which YouTube mentioned a particular search result's ID and concatenate that inside a prefabricated YouTube URL.

Because I wanted the user to retain the ability to override this fetch [in the case of a bad fetch], the storage for these URL's remains that of the full YouTube URL string. The switch to an embed is done with JavaScript via modal.js.