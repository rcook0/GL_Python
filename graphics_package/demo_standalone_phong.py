import argparse
from shapes import make_shapes_dict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shape", choices=["cube", "tetrahedron", "cone", "sphere", "torus"], default="sphere")
    parser.add_argument("--frames", type=int, default=60)
    parser.add_argument("--gif", help="Output GIF file")
    parser.add_argument("--png-dir", help="Directory for per-frame PNGs")
    parser.add_argument("--size", default="256x256", help="Image resolution WxH")
    # Common lighting params (you already planned)
    parser.add_argument("--ambient", type=float, default=0.2)
    parser.add_argument("--light", nargs="+", action="append", help="Directional light dx dy dz [color]")
    parser.add_argument("--point", nargs="+", action="append", help="Point light px py pz [color]")
    parser.add_argument("--specular", type=float, default=0.5)
    parser.add_argument("--shininess", type=int, default=32)
    # Shape-specific params
    parser.add_argument("--radius", type=float, help="Radius for sphere/torus/cone")
    parser.add_argument("--height", type=float, help="Height for cone")
    parser.add_argument("--R", type=float, help="Major radius for torus")
    parser.add_argument("--r", type=float, help="Minor radius for torus")
    parser.add_argument("--n_lat", type=int, help="Lat subdivisions (sphere)")
    parser.add_argument("--n_lon", type=int, help="Lon subdivisions (sphere)")
    parser.add_argument("--nu", type=int, help="U subdivisions (torus)")
    parser.add_argument("--nv", type=int, help="V subdivisions (torus)")
    args = parser.parse_args()

    shapes = make_shapes_dict()
    shape_fn = shapes[args.shape]

    # Dispatch with shape-specific params
    if args.shape == "sphere":
        polys = shape_fn(
            radius=args.radius or 1.0,
            n_lat=args.n_lat or 16,
            n_lon=args.n_lon or 32
        )
    elif args.shape == "torus":
        polys = shape_fn(
            R=args.R or 1.0,
            r=args.r or 0.3,
            nu=args.nu or 32,
            nv=args.nv or 16
        )
    elif args.shape == "cone":
        polys = shape_fn(
            radius=args.radius or 1.0,
            height=args.height or 2.0,
            n=32
        )
    else:
        polys = shape_fn()

    print(f"Generated {len(polys)} polygons for {args.shape}")
    # TODO: call renderer with polys + lights + args

if __name__ == "__main__":
    main()
