# imse (Image Search)
The goal of this project is to experiment with image search techniques for use in the civil engineering and surveying industries. 
__update__: imse will expand to a generic high dimentional data search and aims to explore contrastive representation learning to build search for many domains. 

## Examples of imse in action
[Here](https://www.youtube.com/watch?v=DEC2m7qAmIg&list=PL0CXgB_3GSNdDHycHhvneodTndJwwY-uT) are two examples of using imse to seach large repositories of images. It uses [dask](https://dask.org/) to lazy load images making it scale to 1000's images of even on a regular images. All image embeddings are stored on disk using [faiss](https://github.com/facebookresearch/faiss) which is used to perform the similarity search. Currently imse uses a pretrained resnet to get embeddings. A simclr pretraining option is coming soon! It's showing get promise especially when the dataset under study contains images that are vastly different to the images in imagenet. Using contrastive representation learning the hope is to apply high dimensional search to other domains. Feel free to open issues with suggested domains in which search by sample query would be useful. 

# The initial use case (
Construction of large projects takes years to complete. During this time a large number of site inspections take place. Site engineers take photographs to document certain aspects of construction. These are used to communicate within their team as well as making up a key piece of many reports to clients. Photos taken during construction are also used in investigations when things break or don't last as long.

## The problem
It seems that all these images (growing at approx 300 per day for some projects) are not managed in a useable way. When the client report or and investigation is called for it is common for junior and mid-level engineers to spend hours sifting through photographs looking to see if on captured the feature in question. This wastes a lot of time and produces suboptimal results.
### Motivation 
I saw and heard 2 civil engineers describe the "chaos" of site work and inspections. They both described searching for images to be a mess. Both work in a windows environment.  
I built a stand along tool to grab gps from image metadata and made a .kml file with image thumbnails and links. This makes it easy to search along one axis (Location) and it was very useful. This little project aims to make it easy to search for Content of interest in a bunch of images.   

## Solution
There are 3 axes that one needs to be able to search and filter on to have a useable image search tool. Location (gps tagged images), Time (date taken) and Content (features of importance captured in the image). 
The first two are easy to achieve and have very low risk. The third is where it could get interesting. There are transfer learning, unsupervised and semi-supervised schemes that could work to solve searching the Content axes. 

### A description of what a solution would look like
An application with slick UI to search all images in specified locations (C:// Network://) along the 3 axes. 
A view of the images on a map, a timeline and ranked based on queries.
Constraints: all images must remain on-premise. Application must be easy to install. 
    

# Roadmap
- [ ] Look harder to see if something already exists!
- [ ] Think of a nice deploy/install form factor.
- [ ] Test various image retrieval techniques to see what pathologies may be hard to solve.
- [ ] Think of a commercial angle that could make this project worth doing (from a financial perspective).

# Comments
It feels like there must be a need for image search in a number of small and medium size businesses. I know postgres based image search options but that still needs these rather small or naive teams to integrate such a tool into the way they work. 
Perhaps there are  opportunities in doing search on other high dimension data (music, speeches, laboratory experiment outputs).

Unfortunately all these kinds of issues seem to boil down to just a lot of good old software engineering and design. Perhaps the better option is to build database 'plugins' that would allow any dev house to leverage recent ML techniques (unsupervised).

# Basic usage
0. Modify the mount points in `.devcontainer/devcontainer.json
`

        `"mounts": [
                "source=/home/{USER}/.cache/torch,target=/home/user/.cache/torch,type=bind,consistency=cached", 
                "source=/home/{USER}/.aws,target=/home/user/.aws,type=bind,consistency=cached"
            ],`
1. Open in remote container. 
2. Paste aws creds in `~/.aws/credentials`
3. `dvc pull`
4. `cd src && streamlit run app.py`
