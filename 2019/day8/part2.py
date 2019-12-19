'''
Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data 0222112222120000 corresponds to the following image layers:

Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
Then, the full image can be found by determining the top visible pixel in each position:

The top-left pixel is black because the top layer is 0.
The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
So, the final image looks like this:

01
10
What message is produced after decoding your image?
'''
import os


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        img = f.read()

    layer_size = 25 * 6
    layers = [img[i:i+layer_size] for i in range(0, len(img), layer_size)]

    resulting_img = [2] * layer_size
    for pixel in range(0, layer_size):
        for layer in layers:
            if layer[pixel] != '2':
                resulting_img[pixel] = layer[pixel]
                break
    
    # Print the image (set black to # and other pixels transparent)
    for index, pixel in enumerate(resulting_img):
        # Print newline after each row
        if index % 25 == 0:
            print('')
        if pixel in ['2', '0']:
            print(' ', end ='')
        else:
            print('#', end ='')
    # Print newline to the end
    print()
    
if __name__== '__main__':
    main()

