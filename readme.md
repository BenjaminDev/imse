# imse (Image Search)
The goal of this project is to experiment with image search techniques for use in the civil engineering and surveying industries.

# The Main Ideas
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
- [] Look harder to see if something already exists!
- [] Think of a nice deploy/install form factor.
- [] Test various image retrieval techniques to see what pathologies may be hard to solve.
- [] Think of a commercial angle that could make this project worth doing (from a financial perspective).

# Comments
It feels like there must be a need for image search in a number of small and medium size businesses. I know postgres based image search options but that still needs these rather small or naive teams to integrate such a tool into the way they work. 
Perhaps there are  opportunities in doing search on other high dimension data (music, speeches, laboratory experiment outputs).

Unfortunately all these kinds of issues seem to boil down to just a lot of good old software engineering and design. Perhaps the better option is to build database 'plugins' that would allow any dev house to leverage recent ML techniques (unsupervised).

# Basic usage
1. Open cloned repo in remote container. 
2. Open in 