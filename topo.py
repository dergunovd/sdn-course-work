from mininet.topo import Topo

class MyTopo( Topo ):
    "Network topology"
    
    def __init__( self ):
        Topo.__init__( self )
        
        # Add hosts
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
        host5 = self.addHost( 'h5' )
        host6 = self.addHost( 'h6' )
        host7 = self.addHost( 'h7' )
        host8 = self.addHost( 'h8' )
        host9 = self.addHost( 'h9' )

        # Add switches
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        mainSwitch = self.addSwitch( 's4' )
    
        # Connect 4 hosts to first switch
        self.addLink( host1, switch1 )
        self.addLink( host2, switch1 )
        # Limit bandwidth to 40Mb/s
        self.addLink( host3, switch1, bw=40 )
        self.addLink( host4, switch1 )

        # Connect 4-7 hosts to second switch
        # Limit bandwidth to 20Mb/s
        self.addLink( host4, switch2, bw=20 )
        self.addLink( host5, switch2 )
        self.addLink( host6, switch2 )
        self.addLink( host7, switch2 )

        # Connect 8-9 hosts to third switch
        self.addLink( host8, switch3 )
        self.addLink( host9, switch3 )

        # Connect all switches to main switch
        # Limit bandwidth to 100Mb/s
        self.addLink( switch1, mainSwitch, bw=100 )
        self.addLink( switch2, mainSwitch, bw=100 )
        self.addLink( switch3, mainSwitch, bw=100 )
        
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
