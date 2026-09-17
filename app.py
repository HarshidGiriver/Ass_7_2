def generate_report():
    """Generates a static application report text file."""
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("Application Report\n")
        f.write("Total Users: 200\n")
        f.write("Active Sessions: 45\n")
    
    print("Report generated successfully.")

if __name__ == "__main__":
    generate_report()
