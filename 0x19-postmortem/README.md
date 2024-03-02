<H1 style="text-align: center; border: 0; font-weight: 900;">Power Outage</H1>

## Issue Summary
- Power outage that caused the servers and routers to go down and the services have stopped.
- The outage started on 21/10/2022 at 7:25PM (UTC) and ended almost two hours later at 9:15PM (UTC)
- The outage included 
    - The application servers clusters
    - Database servers
    - All the networking infrastructure related to them
- Due to the outage, all users (100%) lost the access to any dynamic content, but static content serving had no issues at all, as the web servers was located in a different building and weren't affected by the incident
- The power outage was caused by poor electric work and lacking masonry insulations in the neighboring building, which weren't immune to rain water and the heavy rain that day did some severe damage to the electrical connections there and transferred to us through the shared wall.
- Thanks Mr. and Mrs. Neighbors

## Timeline
- 04:13 PM - 21/10/2022: Heavy rain starts<br>
- 06:58 PM - 21/10/2022: Stains of water were noticed on the wall<br>
- 07:25 PM - 21/10/2022: Power went out in the whole building and the site engineer obviously noticed that<br>
- 07:26 PM - 21/10/2022: Site engineer reported the outage to the headquarters<br>
- 07:53 PM - 21/10/2022: Emergencies team arrived and started investigating<br>
- 07:55 PM - 21/10/2022: It was thought that the generator was damaged<br>
- 07:59 PM - 21/10/2022: Thanks to our site engineer efforts in connecting the dots and investigating the issue before the<br>
    &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;
    emergencies team arrival, the cause of the issue was identified quickly, it was the rain combined<br>
    &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;
    with the neigbors' bad masonry and electrical insulation, caused the main circuit breaker<br>
    &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;
    responsible for both the buildings to trip down, which alsoprevented the backup generator from<br>
    &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;
    starting as a safety precaution (Generator control circuit was programmed not to start if the<br>
    &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;
    main circuit breaker is tripped as a safety precaution)<br>
- 08:00 PM - 21/10/2022: After ruling out generator problems, electrical team was summoned to the site<br>
- 08:45 PM - 21/10/2022: The electrical team arrived and started investigating the electricity network<br>
- 08:49 PM - 21/10/2022: They disconnected the generator for the circuit and started it and it was all good<br>
- 08:49 PM - 21/10/2022: They came up with the decision to connect the machines and devices to the generator through a<br>
    &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;
    temporary external electrical network and shunts, so they can fix the main network and cut any<br>
    &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &ensp;
    connections with the lovely neighbors electrical system<br>
- 09:10 PM - 21/10/2022: Installation of the temporary electrical network was done<br>
- 09:10 PM - 21/10/2022: Starting devices and booting up the machines<br>
- 09:15 PM - 21/10/2022: Issue fixed and all services are up and working<br>
- 09:17 PM - 21/10/2022: Celebrating and drinking under the rain<br>
- 10:30 PM - 21/10/2022: Unfortunately, the celebration came to an end :(<br>

## Root cause and resolution
The root cause was that we hadn't dedicated main electricity network, which made us susceptible to external problems. That problem was that our lovely neighbors (they are truly adorable <3) hadn't proper building insulation, had no immunity against severe weather situations and the heavy rain caused the main circuit breaker to trip and that prevented our generator from starting.

The short-term resolution was building a temporary electric network that is connected to the generator and connect the devices to it.

The long-term resolution was building a dedicated electric network (Not shared with any one) and insulating all the walls that is shared with others against all weather conditions.

## Corrective and preventative measures:
- Things to be improved:
    - Preventing any down time by insuring all the essential devices and machines are up and running all the time.
    - Having redundancy to eliminate any electrical SPOF 

- To do list:
    - Connecting all the essential equipment to battery powered UPS devices so they don't go down in case of any power outage even until the generator is up and working.
    - Build a backup electrical network to switch to in case there is any problem with the main one
    - Interviewing any new neighbors about safety, the precaution they take and how careful people are they (JUST KIDDING OF COURSE)
