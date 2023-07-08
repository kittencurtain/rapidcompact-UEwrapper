# rapidcompact-UEwrapper
Authored by Aidan Grant / kittencurtain

This project consists of a basic python wrapper for the RapidCompact CLI to batch-compact multiple 3D files, output them to Unreal-compatible texture formats, and get them ready for import. The UE project is blank except for a master material, which can be instanced for each new imported object/material. The maps for each object can then be plugged into the instance parameters. One mesh and its textures have been imported into the project as an example (see folder "**EXAMPLE**").

**NOTE:** This project is not intended to be production-ready, but is rather a basic test script to wrap and semi-automate the compacting process. There is room for improvement as UE asset files could be auto-generated for each new instance material, and the folder structure of the output heirarchy could be further adjusted to match a given team's structure conventions.

This repo is private and is not meant for distribution. Pull requests will not be overseen.
