import imageio

def create_gif(list_name, gif_name, duration=1):
    frames = []
    for list in list_name:
        nmy = imageio.imread(list)
        frames.append(nmy)

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)

def main():
    list_name = ['../制作 动态图/image/孙悟空.jpg', '../制作 动态图/image/美女.jpeg', '../制作 动态图/image/美女2.jpeg']
    gif_name = '动态.gif'
    create_gif(list_name, gif_name)

if __name__ == '__main__':
    main()
