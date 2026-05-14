import os

def rename_dataset_files(dataset_path="dataset"):
    if not os.path.exists(dataset_path):
        print(f"Error: The folder '{dataset_path}' was not found.")
        return

    for folder_name in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder_name)

        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder_name}...")
            
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            
            files.sort()

            count = 0
            for index, filename in enumerate(files, start=1):
                file_extension = os.path.splitext(filename)[1]
                
                new_name = f"{folder_name}_{index}{file_extension}"
                
                old_file_path = os.path.join(folder_path, filename)
                new_file_path = os.path.join(folder_path, new_name)
                
                os.rename(old_file_path, new_file_path)
                count += 1
                
            print(f"  -> Renamed {count} files in '{folder_name}'.")

if __name__ == "__main__":
    rename_dataset_files()
    print("\nAll files renamed successfully!")
    