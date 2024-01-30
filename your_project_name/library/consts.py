import pkg_resources

package_name = "your_project_name"
version = pkg_resources.get_distribution(package_name).version
