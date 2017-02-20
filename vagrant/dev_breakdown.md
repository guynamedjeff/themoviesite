# Development Breakdown

Over the course of development, The Movie Site went through many feature changes along the way. The more interesting parts include video modals which I had no prior experience with and the Redis cache which required JSON encoding/decoding.

This all took place over the course of a few weeks before authoring this breakdown; however, the site continues to gain features and undergo stylistic changes. The latest was the initially-planned ability to fetch YouTube URL's for new movies rather than input them manually.

The primary issue with that was a lack of practice, but it was ultimately pretty straight forward. I simply had to find the various means in which YouTube mentioned a particular search result's ID and concatenate that inside a prefabricated YouTube URL.

Because I wanted the user to retain the ability to override this fetch [in the case of a bad fetch], the storage for these URL's remains that of the full YouTube URL string. The switch to an embed is done with JavaScript via modal.js.

# Update 2/20/17:

Today marked the introduction of poster URL pulls, removing yet another field in the 'add movie' section with the goal of limiting user workload. This was done with an IMDB regex search after the more tradition approach of using python's 'find' method proved unnecessarily difficult.

Future integration plans include storing the images server-side after the fetch, so simple users no longer bother Amazon for poster data. Furthermore, the planned automated downscaling for these images will reduce my own server load and speed up client-side renders.

In regards to further fetching, there are no current plans to go beyond what is already implemented. Secondary options for pulling trailer and poster URL's would be a plus, however, grabbing other data such as descriptions may skirt the boundary of plagiarism as there is no unified source of official movie synopses.