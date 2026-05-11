from parsers.jd_parser import save_all_structured_jds


output_files = save_all_structured_jds("data/JD", "data/structured_jds")

print(f"Structured JD files created: {len(output_files)}")

for output_file in output_files[:5]:
    print(output_file)
