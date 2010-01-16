import mpl_toolkits.ps_cmyk

imshow(np.arange(100).reshape(10,10))

savefig("a.eps", format="eps_cmyk")

