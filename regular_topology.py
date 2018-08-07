import sys, getopt, os

if len(sys.argv) < 3:
    print ('invalid args');
    sys.exit(0);

topology = {'random', 'mesh', 'torus'}


if sys.argv[1] not in topology:
    print ('please input correct topology:');
    sys.exit(0);

if int(sys.argv[2]) < 1:
    print ('please input correct number');
    sys.exit(0);

current_dir = os.getcwd();
object_dir = current_dir + '/platform';

if (not os.path.exists(object_dir)):
    os.makedirs(object_dir);
    print ("create " + object_dir + " successfully!");


print (topology, type(topology));
print (sys.argv[1]);
print (sys.argv[2]);


print(current_dir);
print(object_dir);






























