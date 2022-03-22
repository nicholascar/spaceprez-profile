# SpacePrez Profile
This is a data *profile* defined to capture the data requirements of the *SpacePrez* tool.

*SpacePrez* is the spatially-configured [Prez](https://github.com/surroundaustralia/Prez/) application.

Note that most of the constraints that this profile places on data are inherited from the [OGC LDA PI Profile](https://w3id.org/profile/ogcldapi) which ensures RDF spatial data is formulated according to [GeoSPARQL 1.1](https://opengeospatial.github.io/ogc-geosparql/geosparql11/spec.html) and that it has all the elements needed for [OGC API - Features Core](https://ogcapi.ogc.org/features/) APIs.  

This data profile has a persistent web address identifier:

* <https://w3id.org/profile/spaceprez>

## Profile Resources

### Specification
This profile's _specification_ - the resource that contains its normative rules - is within the file [specification.html](specification.html) and it is able to be viewed online at:

* <https://w3id.org/profile/spaceprez/spec>


### Validator
This profile's rules, as defined in the _specification_, are presented for machine validation of RDF data in the shapes file [validator.shacl.ttl](validator.shacl.ttl) which conforms to the [SHACL](https://www.w3.org/TR/shacl/) standard.

Tools such as [pySHACL](https://github.com/RDFLib/pySHACL) and the online [SHACL Playground](https://shacl.org/playground/) or [SHACL Play!](https://shacl-play.sparna.fr/play/) can be used with this shape file to validate vocabulary files.

The validator can be accessed directly at 

* <https://w3id.org/profile/spaceprez/validator>


## License  
This code is licensed using the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) licence. See the [LICENSE file](LICENSE) for the deed. 

Note [Citation](#citation) below for attribution.


## Citation
To cite this profile, please use the following (formulated in [BibTex](http://www.bibtex.org/)):

```
@software{spaceprez-profile,
  author = {{SURROUND Australia Pty Ltd}},
  title = {{SpacePrez Profile}},
  version = {1.0},
  date = {2022},
  publisher = {{SURROUND Australia Pty Ltd}},
  url = {https://w3id.org/profile/spaceprez}
}
``` 


## Contact
*publisher:*  
![](style/SURROUND-logo-100.png)  
**SURROUND Australia Pty. Ltd.**  
<https://surroundaustralia.com>  

*creator:*  
**Dr Nicholas J. Car**  
*Data Systems Architect*  
SURROUND Australia Pty. Ltd.  
<nicholas.car@surroudaustralia.com>  
<https://orcid.org/0000-0002-8742-7730>