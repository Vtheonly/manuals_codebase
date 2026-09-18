from compiler import build
if __name__ == "__main__":
    manifest=build()
    print(f"Built {len(manifest['artifacts'])} independent visual artifacts.")
    print("Outputs are in ./output")
