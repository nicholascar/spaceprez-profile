"""Converts GeoSPARQL geometry data in WKT form to GeoJSON

A Python script to convert GeoSPARQL WKT geometry data to GeoJSON as GeoJSON data is required by the SpacePrez tool.

Run the help command on the tool to see command

"""

import argparse
from pathlib import Path

from rdflib import Graph, Namespace, Literal
from shapely.wkt import loads as wkt_load
from shapely_geojson import dumps as jdumps

GEO = Namespace("http://www.opengis.net/ont/geosparql#")


def convert(rdf_file_path: Path, retain: bool = True):
    g = Graph().parse(rdf_file_path)

    for geom, wkt_lit in g.subject_objects(GEO.asWKT):
        g.add((geom, GEO.asGeoJSON, Literal(jdumps(wkt_load(wkt_lit)), datatype=GEO.geoJSONLiteral)))
        if not retain:
            g.remove((geom, GEO.asWKT, wkt_lit))

    return g


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        help="Input file location or URL",
    )

    parser.add_argument(
        "-r",
        "--retain",
        help="Whether (true) or not (false) to retain the original WKT geometry data",
        choices=["true", "false"],
        default="true",
    )

    parser.add_argument(
        "-o",
        "--outputfile",
        help="A name you wish to assign to an output file. If not supplied, output will be text to standard out",
        default=None,
    )

    args = parser.parse_args()

    p = Path(args.input)

    if not p.exists():
        print("The file path you entered does not exist.")
        exit()

    understood_files = [".ttl"]
    if p.suffix not in understood_files:
        print(f"The file you've indicated is not understood (must end with {', '.join(understood_files)}).")
        exit()

    g = convert(Path(args.input), True if args.retain == "true" else False)

    if args.outputfile is not None:
        g.serialize(destination=args.outputfile, format="longturtle")
    else:
        print(g.serialize(format="longturtle"))


if __name__ == "__main__":
    main()
