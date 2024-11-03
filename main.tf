# main.tf

provider "aws" {
  region = "us-west-2" 
}

resource "aws_s3_bucket" "firetracker_bucket" {
  bucket = "firetracker-terraform-bucket"
  acl    = "private"

  tags = {
    Name        = "FireTrackerBucket"
    Project     = "FireTracker"
    Environment = "Dev"
  }
}

resource "aws_security_group" "firetracker_sg" {
  name        = "firetracker_sg"
  description = "Security group for FireTracker EC2 instance"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "FireTrackerSG"
    Project = "FireTracker"
  }
}

resource "aws_instance" "firetracker_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.firetracker_sg.name]

  tags = {
    Name = "FireTrackerInstance"
    Project = "FireTracker"
    Environment = "Dev"
  }
}

output "firetracker_instance_public_ip" {
  value = aws_instance.firetracker_instance.public_ip
  description = "Public IP address of the FireTracker EC2 instance"
}
