/* 	$Id: PolyUtil.h 69 2010-03-17 19:54:10Z jraedler $	 */
#ifndef POLY_UTIL_H
#define POLY_UTIL_H

#include "gpc.h"

/* operations on polygons */
gpc_polygon * poly_p_new(void);
int    poly_p_clone(gpc_polygon *, gpc_polygon *);
double poly_p_area(gpc_polygon *);
int    poly_p_center(gpc_polygon *, double *, double *);
int    poly_p_point_inside(gpc_polygon *, double, double);
void   poly_p_boundingbox(gpc_polygon *, double*, double*, double*, double*);
void   poly_p_shift(gpc_polygon *, double, double);
void   poly_p_scale(gpc_polygon *, double, double, double, double);
void   poly_p_rotate(gpc_polygon *, double, double, double);
void   poly_p_warpToBox(gpc_polygon *, double, double, double, double, double *);
void   poly_p_flip(gpc_polygon *, double);
void   poly_p_flop(gpc_polygon *, double);

/* operations on single contours */
double poly_c_area(gpc_vertex_list *);
int    poly_c_center(gpc_vertex_list *, double *, double *);
int    poly_c_point_inside(gpc_vertex_list *, double, double);
void   poly_c_boundingbox(gpc_vertex_list *, double*, double*, double*, double*);
int    poly_c_orientation(gpc_vertex_list *);
#endif /* POLY_UTIL_H */
