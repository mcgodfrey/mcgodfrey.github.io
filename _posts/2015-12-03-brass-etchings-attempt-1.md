---
title: 'Brass etchings &#8211; attempt 1'
date: '2015-12-03T23:06:10+00:00'
author: matt
layout: post
permalink: /2015/12/03/brass-etchings-attempt-1/
image: /img/2016/01/finished-product1-e1588213139607.jpg
categories:
    - Projects
---

Cleaning out the garage I found/rediscovered some brass sheets which have been sitting there for quite a while, so my first thought was to attempt etching them to make some art. A quick internet search revealed two options, chemical acid etching or electrochemical etching. I decided on the electrochemical route because it seems safer (no nasty acids) and cooler (who doesn't love a battery with wires running to electrodes in a bath of blue water?). I'll start with a teaser photo of the results of this first attempt, and then go into some details.

![finished](/img/2016/01/finished-product.jpg)

The finished product after etching, painting and sanding back

## Background
Electrochemical etching is the opposite/companion process to electroplating, where a current is passed between two electrodes in an electrolyte which results in oxidation (etching) at the positive electrode and reduction (plating) at the negative electrode. The etch rate is directly proportional to the current – for each electron which is forced through the circuit, one atom is removed from the positive electrode and plated onto the negative one. While it is not strictly necessary, it is usual for both electrodes and the cation in the electrolyte to be all the same metal. While it is possible to use other electrolytes for example, this can cause problems and result in additional unwanted reactions and unwanted metals being deposited on the negative electrode. It will also change the composition of the solution over time as different cations are released and plated onto the electrodes.

In order for the etching to be used to create patterns, areas of the electrode need to be masked to protect them from etching. This mask needs to form a physical barrier between the metal and the electrolyte. So, it needs to be able to stick to the surface, form a barrier to water and be able to be easily applied in potentially intricate shapes. There are two basic methods which people seem to use. The first is the simplest and uses a marker or paint to draw the mask by hand directly on the metal surface. The second method involves transferring the toner from a laser printer onto the surface – you basically print the mask and then use heat (from an iron for example) to melt the toner and transfer it to the metal. There are examples of this method on the net, for example here. For my initial testing though I have decided to go with the first method for its simplicity.

## Initial sample preparation

First I cut some small rectangular pieces from the brass sheet roughly 5x10cm (the sheet is 1.6mm thick) using a hacksaw and cleaned up/deburred the edges. These were then cleaned to remove any dust, oxide, grease, etc. in soapy water with a dish sponge, using the scourer side to really clean the surface. It made fine scratch marks on the surface and I scrubbed in perpendicular directions to really clean and roughen up the surface to give my mask something to stick to.

With the surfaces clean, it was time to add the mask. My first attempt used a permanent marker (sharpie brand) to draw my shape directly onto the brass. (Note that the drawings  in this post are of the Amber Gambler, the one-time logo of a beer we made who has now reached almost mythical status in its own right). As can be seen in the pictures, there wasn’t a very thick coverage. I tried waiting for it to dry and reapplied to try to make it thicker but without much success. As you’ll see later, the sharpie experiment was fairly unsuccessful, so I ended up re-cleaning and going over the original mask with some regular house paint.

![masking](/img/2016/01/masks.png)

Three masking techniques. (Top left) permanent “sharpie” marker, (top right) house paint, (bottom) paper mask with enamel spray paint (the paper was peeled off to expose the metal after the paint had dried)

For the second sample I decided to try a negative mask, ie. just etching the outline and leaving everything else unetched. I printed the shape onto regular paper, cut out the lines and glued them to the sample with wood glue. I then coated the entire thing with an enamel spray paint, let it dry and peeled off the paper, leaving everything covered except the lines. This required a bit of extra work to clean up the metal surface afterwards to remove some residual glue. Also the edges were not as sharp as I would have liked as some of the paint came off with the paper mask. It might be better next time to run a knife around the edges first.

For both samples I stripped the end of a ~20cm piece of multicore wire (apparently ~15A rated) , splayed the end and used electrical tape to stick it to the backside. I then covered the entire backside in electrical tape to prevent it from etching and to hold the wire in place. The other end of the wire was attached to my power supply, described below.

![ready for etching](/img/2016/01/wires-attached.png)

The piece is ready for etching with the wire taped to the backside

## Equipment setup

Etching was performed in a plastic container~10x20cm and 10cm deep. Since the sample is brass, which is mostly copper (plus Zinc and a often a small amount of Lead), I used copper sulfate (CuSO4) as my electrolyte and a piece of copper pipe as my negative electrode. I picked up the Copper Sulfate from Bunnings for ~$10 for 500g. Apparently you can use a whole range of different salts for the electrolyte, including normal table salt according to some people. I decided to go with Copper Sulfate as it is cheap enough and it seemd like the safest route. Also, the electrolyte is not consumed so it can be reused almost indefinitely.

![setup](/img/2016/01/solution-setup.png)

Shows the etch bath setup with copper sulfate solution. On the right is the solution resistance (~400Ohms) measured with a multimeter and the probes ~10mm apart. This was the lowest resistance I could achieve which I assume means that the solution was saturated.

I filled the container with water and added CuSO4 a few tablespoons at a time, stirring to dissolve between each addition. After each addition I measured the resistance of the solution  over ~10mm by dipping the multimeter probes directly into the solution. It started up in the MOhm range and kept decreasing down to a few hundred ohms where it saturated. I figured that this meant I had saturated the solution so I stopped.

![full setup](/img/2016/01/full-setup.png)

This shows the full setup. On the left is the battery charger and multimeters to monitor the current and voltage. The right shows how the electrodes are positioned in the bath

Finally, all that was left was to hook everything up. The copper pipe  was clamped in the liquid at one end of the bath. The sample was placed at the other end, and the 2 electrodes were attached to my power supply (the copper pipe to the negative terminal, the sample to the positive one). For the power supply I tried two different options – a 12V battery charger with a maximum current of 2.5A and a 12V car battery. I also attached a couple of multimeters to measure the voltage over the 2 electrodes and the current.

## Etching

I initially started with the battery charger as the 2.5A maximum output meant that there was less potential for causing damage (both to me and the battery). There was not a lot of activity – some slight bubbling and visible water currents around the sample but nothing spectacular. I couldn’t get a good measurement of the current because the resistance on my multimeter leads was too high. But, the voltage measured over the electrodes was only ~6-7V which indicates that it had reached it’s current limit of ~2.5A. Moving the electrodes closer and further apart altered the voltage (as the resistance through the electrolyte changed) but it was always under 12V.

After about 20 minutes I removed the first sample (with the sharpie mask) to inspect it. There was a layer of brown material over the etched regions which came away very easily  in large sheets by rubbing it or just stirring it through the water. The material had etched slightly, but it was very shallow so I decided to move up to the battery. More problematic though, the sharpie mask was not doing a very good job at masking… The regions where the marker was visibly thinner had started etching and the marker had lifted up from the metal in some places. So, this prompted the move to the paint mask. I removed, cleaned and repainted the mask using regular house paint and continued etching.

![first etch](/img/2016/01/first-etch.jpg)

After about 20 minutes of etching at 2.5A. Note the regions where the brass is showing through the green marker mask. This prompted a rethink and the new paint mask

Things progressed much more quickly with the battery. I couldn’t get a good measurement of the current but I’m guessing somewhere in the order of 10A, although this changed depending on the electrode separation. With the battery I was getting pretty much the full unloaded voltage over the electrodes, with a slight drop when if I moved them very close together. I pulled out the sample and inspected it every 10 minutes or so and after about an hour I was fairly happy with the etch depth and moved on to the second sample. The paint mask was also starting to lift up in some places so it was time to stop the etch anyway. The second sample etched more quickly, presumably due to the smaller area which was being etched. It was finished in about 30 minutes.

![after etch](/img/2016/01/finished-etching.jpg)

The two pieces after etching. The etch depth is about 0.1mm for both. Note that there is not a lot of contrast between the etched and unetched regions, and this became worse after a thorough clean

## Finishing up

Etching complete, all that was left was to finish up the pieces. First step was to remove the mask and clean up the surface which I did by sanding with 240 grit sandpaper and a sanding block (offcut piece of wood). That done I was back to bare metal with my etched pattern. There was not a lot of contrast between the etched and unetched regions so in order to get it to stand out I wanted to fill the etched regions with black paint. To this end I coated the whole sample in black enamel spray paint and then sanded off just the raised, unetched regions, again with 240 grit sandpaper and a sanding block.

And the finished product:

![finished product](/img/2016/01/finished-product.jpg)

The finished product after etching, painting and sanding back

## Final thoughts

Overall I think it was fairly successful for a first attempt – they turned out looking quite reasonable despite the very simple masking technique. The etch edges are quite rough, but I think that can be improved by optimising the masking. I would also like to try the toner transfer method to see if that works any better. I was impressed with how well the final step of blackening the etched regions worked. There are a few blemishes and regions where I’ve slightly sanded the etched areas but I think they add to the overall look (I can justify it that way anyway).

Some final comments and ideas for improvement:

- A good mask is very important. It needs to withstand the water and etching without peeling or etching through. Related to this, I would like to be able to define sharper edges. The toner transfer method may help here.
- The sharpie was definitely not good as a mask. I would like to try again with a much thicker permanent marker as this seems to be by far the easiest method to quickly define the mask.
- It may be worth giving the surface a more thorough clean before applying the mask to help it stick. Maybe some IPA after the soapy water clean. Possibly even an initial light sand to roughen up the surface.
- Relatively large currents are required to achieve a reasonable etch rate. 2.5A was nowhere near enough. The battery was much better, but next time I would like to monitor the current during the etch.