from PIL import Image   #pip install pillow or pip install --user pillow

input_image = "4 imgtograyscale\\input.jpg"  
output_image = "4 imgtograyscale\\output_grayscale.jpg" 

def convert_to_grayscale(input_path, output_path):
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert the image to grayscale
        grayscale_img = img.convert('L')
        
        # Save the grayscale image
        grayscale_img.save(output_path)
        grayscale_img.show()
        print(f"Image successfully converted and saved to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


convert_to_grayscale(input_image, output_image)